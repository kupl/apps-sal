from sys import stdin, stdout


H, L = [int(x) for x in stdin.readline().split()]

ans = (float)(L * L - H * H) / (2 * H)
print(ans)
