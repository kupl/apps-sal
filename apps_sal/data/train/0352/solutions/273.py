class Solution:

    def __init__(self):
        self.results = []
        self.explored = dict()

    def traverse(self, string, listt, buffer):
        flag = True
        for i in range(len(string)):
            if string[:i] + string[i + 1:] in listt:
                flag = False
                self.traverse(string[:i] + string[i + 1:], listt, buffer + [string[:i] + string[i + 1:]])
        if flag:
            self.results.append(buffer)
            for item in buffer:
                self.explored[item] = True
        return

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        for word in words:
            if word not in self.explored:
                self.traverse(word, words, [word])
        return len(max(self.results, key=len))
