class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        self.words = words
        self.result = result
        self.front_chars = set([word[0] for word in words] + [result[0]])
        self.result_indices = []
        self.all_chars = []
        new_words = words + [result]
        while len(new_words) > 0:
            for i in range(len(new_words)):
                self.all_chars.append(new_words[i][-1])
                new_words[i] = new_words[i][:-1]
            self.result_indices.append(len(self.all_chars) - 1)
            new_words = [word for word in new_words if len(word) > 0]
        self.mappings = {}
        self.used_chars = set()
        return self.backtrack(0, 0)

    def backtrack(self, current_i: int, carry: int) -> bool:
        if current_i == len(self.all_chars):
            return True
        cur_char = self.all_chars[current_i]
        if current_i in self.result_indices:
            (code, new_carry) = self.verify(self.result_indices.index(current_i), carry)
            if code == 0:
                return False
            else:
                if self.backtrack(current_i + 1, new_carry):
                    return True
                if code == 2:
                    self.used_chars.remove(self.mappings[cur_char])
                    del self.mappings[cur_char]
                return False
        if cur_char in self.mappings:
            return self.backtrack(current_i + 1, carry)
        for i in range(10):
            if cur_char in self.front_chars and i == 0:
                continue
            if i not in self.used_chars:
                self.mappings[cur_char] = i
                self.used_chars.add(i)
                if self.backtrack(current_i + 1, carry):
                    return True
                del self.mappings[cur_char]
                self.used_chars.remove(i)
        return False

    def verify(self, index: int, carry: int) -> (int, int):
        cur_sum = carry
        for word in self.words:
            if index < len(word):
                cur_sum += self.mappings[word[index * -1 - 1]]
        carry = int(cur_sum / 10)
        cur_sum = cur_sum % 10
        result_char = self.result[index * -1 - 1]
        if result_char in self.mappings:
            if self.mappings[result_char] != cur_sum:
                return (0, 0)
            else:
                return (1, carry)
        else:
            if cur_sum in self.used_chars:
                return (0, 0)
            if result_char in self.front_chars and cur_sum == 0:
                return (0, 0)
            self.mappings[result_char] = cur_sum
            self.used_chars.add(cur_sum)
            return (2, carry)
