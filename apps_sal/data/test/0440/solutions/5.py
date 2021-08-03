input()
s = input()
g = {'a', 'e', 'o', 'i', 'u', 'y'}
done = False
while not done:
    done = True
    for i in range(1, len(s)):
        if s[i] in g and s[i - 1] in g:
            done = False
            s = s[:i] + s[i + 1:]
            break
print(s)
