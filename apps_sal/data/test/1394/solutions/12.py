s = input().strip()
a = s.count('a')
n = len(s)

l = (a+n)//2
word = s[:l]
gen = word + word.replace('a', '')

if gen == s:
    print(word)
else:
    print(":(")



