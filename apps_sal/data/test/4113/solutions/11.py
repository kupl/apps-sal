n = int(input())
s = 'No'

for i in range(26):
    for j in range(16):
        total = 4*i +7*j
        if total == n:
            s = 'Yes'
            break
    if total ==n:
        break
print(s)
