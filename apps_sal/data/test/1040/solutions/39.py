n = int(input())
s = list(input())

cnt = 0

while True:
    for i in range(cnt, len(s)-2):
        if s[i:i+3] == ['f', 'o', 'x']:
            del s[i:i+3]
            cnt = max(0, i-3)
            break
    else:
        break
    
print((len(s)))

