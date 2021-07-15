def main():
  K = int(input())
  ans = False
  if K % 2 == 0:
    print(-1)
    return
  cnt = 7 % K
  for i in range(1, K+1):
    if cnt == 0:
      ans = True
      print(i)
      return
    cnt = (10 * cnt + 7) % K
  if ans == False:
    print(-1)
    return
main()
