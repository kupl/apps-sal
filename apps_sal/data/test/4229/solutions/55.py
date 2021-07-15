N =int(input())
a = ""
sum = 0
for i in range(N+1):
#  if(i%15 == 0): a = "FizzBuzz"
  if(i%3 == 0): a ="Fizz"
  elif(i%5 == 0): a = "Buzz"
  else:
    sum =  sum + i
print(sum)
