N = int(input())
(S, T) = map(str, input().split())
kougo = ''
for (s, t) in zip(S, T):
    kougo += s + t
print(kougo)
