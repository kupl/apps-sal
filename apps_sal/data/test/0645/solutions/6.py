s = input()
r = 0
for i in s:
    if not i in '02468qwrtyplkjhgfdszxcvbnm':
        r += 1
print(r)
