class Trie:

    def __init__(self):
        self.letter___node = {}
        self.words_nr = 0

    def add_word(self, word):
        word = word + '$'
        curr_node = self
        for letter in word:
            if letter not in curr_node.letter___node:
                curr_node.letter___node[letter] = Trie()
            curr_node.words_nr += 1
            curr_node = curr_node.letter___node[letter]

    def check_word(self, word):
        word = word + '$'
        curr_node = self
        for letter in word:
            if letter not in curr_node.letter___node:
                return False
            curr_node = curr_node.letter___node[letter]
        return True

    def count_word(self, word):
        word = word + '$'
        curr_node = self
        curr_state = 0
        presses_saved = 0
        for letter in word:
            if letter not in curr_node.letter___node:
                if curr_state == 1:
                    if '$' in curr_node.letter___node:
                        return min(len(word) - 1, len(word) - 1 - presses_saved + 1)
                    else:
                        return len(word) - 1
                if curr_state == 0:
                    return len(word) - 1
            if curr_node.words_nr > 1:
                curr_node = curr_node.letter___node[letter]
            elif curr_node.words_nr == 1:
                if curr_state == 0:
                    curr_state = 1
                presses_saved += 1
                curr_node = curr_node.letter___node[letter]
            elif curr_node.words_nr == 0:
                if curr_state == 1:
                    return min(len(word) - 1, len(word) - 1 - presses_saved + 1)
                elif curr_state == 0:
                    return len(word) - 1
        if curr_node.words_nr == 0:
            presses_saved -= 1
            if curr_state == 1:
                return min(len(word) - 1, len(word) - 1 - presses_saved + 1)
            elif curr_state == 0:
                return len(word) - 1


text = ''
while 1:
    try:
        line = input()
        if line == '':
            raise Exception('e')
        text += line + '\n'
    except:
        break
ans = 0
syms = ['\n', '.', ',', '?', '!', "'", '-']
for sym in syms:
    text = text.replace(sym, ' ')
ans += text.count(' ')
idx___word = text.split(' ')
root = Trie()
root.add_word('$')
root.add_word('$$')
for word in idx___word:
    if word == '':
        continue
    count = root.count_word(word)
    check = root.check_word(word)
    ans += count
    if not check:
        root.add_word(word)
print(ans)
