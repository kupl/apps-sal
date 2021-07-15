n = int(input())
a = input()
alphabet = {}
for i in a:
    alphabet.update({i: a.count(i)})
for i in range(n-1):
    b = input()
    for j in alphabet:
        alphabet[j] = min(alphabet[j], b.count(j))
ans = []
for i in alphabet:
    ans += [i]*alphabet[i]
print((''.join(sorted(ans))))
    
    
    

