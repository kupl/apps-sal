# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
S = [ord(c) - ord('a') for c in input()[:-1]]
T = [ord(c) - ord('a') for c in input()[:-1]]

ans = []
p = N - 1
bemp = S[p] + T[p]
while p > 0:
    p -= 1
    bemp += (S[p] + T[p]) * 26
    ans.append(chr((bemp // 2) % 26 + ord('a')))
    bemp //= 26
ans.append(chr((bemp // 2) % 26 + ord('a')))
print("".join(map(str, reversed(ans))))
