MOD = 10 ** 9 + 7


def main(S, T):
  l = len(T) + 1
  dp = [0] * l
  # sdp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

  # for i, s in enumerate(S):
  #  for j, t in enumerate(T):
  #    v = sdp[i][j + 1] + sdp[i + 1][j] + (1 if s == t else -sdp[i][j])
  #    sdp[i + 1][j + 1] = v % MOD
  for i, s in enumerate(S):
    tmp = [0] * l
    for j, t in enumerate(T):
      v = dp[j + 1] + tmp[j] + (1 if s == t else -dp[j])
      tmp[j + 1] = v % MOD
    dp = tmp

  # return (sdp[-1][-1] + 1)
  return dp[-1] + 1


def __starting_point():
  if True:
    _, _ = map(int, input().strip().split())
    S = input().strip().split()
    T = input().strip().split()
  else:
    S = range(1000)
    T = range(1000)
  print(main(S, T))
__starting_point()
