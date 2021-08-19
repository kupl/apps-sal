(n, k) = map(int, input().split())
s = list(input())
s[k - 1:k] = ''.join(s[k - 1:k]).lower()
print(''.join(s))
