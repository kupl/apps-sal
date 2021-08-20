class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        longest_word = max([len(word) for word in words])
        if len(result) != longest_word and len(result) != longest_word + 1:
            return False
        result_indices = []
        acc = 0
        all_chars = []
        front_indices = []
        for i in range(1, longest_word + 1):
            for word in words:
                if i == len(word):
                    front_indices.append(acc)
                if i <= len(word):
                    all_chars.append(word[i * -1])
                    acc += 1
            if i == len(result):
                front_indices.append(acc)
            result_indices.append(acc)
            acc += 1
            all_chars.append(result[i * -1])
        if len(result) > longest_word:
            result_indices.append(acc)
            front_indices.append(acc)
            all_chars.append(result[0])
        self.words = words
        self.result = result
        self.result_indices = result_indices
        self.all_chars = all_chars
        self.mappings = {}
        self.used_chars = set()
        self.front_indices = front_indices
        return self.backtrack(0, 0)

    def backtrack(self, current_i: int, carry: int) -> bool:
        if current_i == len(self.all_chars):
            if self.mappings[self.result[0]] == 0:
                return False
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
            if current_i in self.front_indices and self.mappings[cur_char] == 0:
                return False
            return self.backtrack(current_i + 1, carry)
        for i in range(10):
            if current_i in self.front_indices and i == 0:
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
            self.mappings[result_char] = cur_sum
            self.used_chars.add(cur_sum)
            return (2, carry)
