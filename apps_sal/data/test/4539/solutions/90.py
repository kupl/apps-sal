def digit_sum(num):
    total_num=0
    while num>0:
        total_num+=num % 10
        num//=10
    return total_num

N=int(input())
if N%digit_sum(N)==0 :
  print("Yes")
  return
print("No")
