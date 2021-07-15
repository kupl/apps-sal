string = [e for e in input()]
n = int(input())

for i in range(n):
    l, r, k = map(int, input().split())
    l -= 1
    r -= 1    
    k %= r - l + 1
    old_string = string[l:r + 1]
    for j in range(l, r + 1):
        string[j] = old_string[j - l - k]
    
print(''.join(string))
