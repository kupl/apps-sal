def sum(n):
  return (n*(n+1))//2
N=int(input())
fizz_cnt=N//3
buzz_cnt=N//5
fizzbuzz_cnt=N//15
print(sum(N)-sum(fizz_cnt)*3-sum(buzz_cnt)*5+sum(fizzbuzz_cnt)*15)
