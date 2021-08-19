n = int(input())
(s, t) = input().split()
print(''.join([S + T for (S, T) in zip(s, t)]))
