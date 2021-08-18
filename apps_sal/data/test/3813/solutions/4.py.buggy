# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = list(map(int, readline().split()))
*p, = list(map(int, readline().split()))
*x, = list(map(int, readline().split()))

dp = [1] * n
z = [0] * n

for i in range(n - 1, -1, -1):
    # print(i,x[i],(z[i],(dp[i].bit_length()-1)),bin(dp[i])[2::][::-1])
    if dp[i] == 0:
        # print(i)
        # print(dp)
        # print(z)
        print("IMPOSSIBLE")
        return

    y = dp[i].bit_length() - 1
    # (z[i]-y,y) を (z[i]-y,x)にするのが最善

    if i == 0:
        # print(dp)
        # print(z)
        print("POSSIBLE")
        return
    else:
        pi = p[i - 1] - 1
        v = dp[pi]
        dp[pi] = ((v << x[i]) | (v << (z[i] - y))) & ((1 << (x[pi] + 1)) - 1)
        z[pi] += x[i] + z[i] - y
