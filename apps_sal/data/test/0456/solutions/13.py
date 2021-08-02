n = int(input())
text = input()
parazit = ''
for i in range(n):
    if text[i:i + 3] == 'ogo':
        parazit = 'o'
        while text[i + 1:i + 3] == 'go':
            parazit += text[i + 1:i + 3]
            i += 2
        text = text.replace(parazit, '***', 1)
print(text)
