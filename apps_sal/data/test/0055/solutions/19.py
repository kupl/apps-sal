n, k = map(int, input().split())

s = list()
b = list()
base = 0
while n > 0:
    s.append(n%2)
    b.append(base)
    n //= 2
    base += 1
s.reverse() # indicate existence
b.reverse() # indicate which power of 2
# print(s)
# print(b)

t = sum(s)
if t > k:
    print('No')
    return
    
pos = 0
while t < k:
    if pos+1 == len(s): # extend if necessary
        s.append(0)
        b.append(b[-1] - 1)

    if t + s[pos] <= k:
        t += s[pos]
        s[pos+1] += 2 * s[pos]
        s[pos] = 0
        pos += 1        
    else:       
        for i in range(len(s)-1, -1, -1):
            if s[i] > 0:
                while t < k:
                    if i+1 == len(s):
                        s.append(0)
                        b.append(b[-1] - 1)                    
                    s[i] -= 1
                    s[i+1] += 2
                    t += 1
                    i += 1
                break

res = list() # comply with answer form
for i in range(len(s)):
    for j in range(s[i]):
        res.append(b[i])
print('Yes')
print(' '.join(map(str, res)))        
