def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 一旦 A[i] - i + 1 を計算する。
  # A[i] が正の時、b を正にすると abs が b 分減る。
  # A[i] が負の時、b を負にすると abs が b 分減る。
  # A[i] が0の時、b abs はどうやっても増える。
  # つまり 正と負とゼロの A[i] を数えて、それぞれ plus, minus, zero とすると、
  # abs は b*(plus-minus) + abs(b)*zero 分増える。
  for i in range(N): A[i]-=i+1
  A.sort()
  if len(A)%2:
    b=A[len(A)//2]
  else:
    b=round((A[len(A)//2]+A[len(A)//2-1])//2)
  ans = 0
  for i in range(N):ans += abs(A[i]-b)
  # print(A, average_A)
  print(ans)

resolve()
