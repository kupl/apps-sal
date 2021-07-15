N = int(input())
S = input()
ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = [ss[(ss.index(s)+N)%26] for s in S]
print(("".join(ans)))

