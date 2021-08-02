n, k = list(map(int, input().split()))
s = list(input())
s[k - 1] = chr(ord(s[k - 1]) + ord('a') - ord('A'))
print((''.join(s)))
