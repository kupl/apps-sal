def main():
   N=int(input())
   CONST= 10**9+7
   Output = 0
   lis = list(map(int,input().split()))       
   lis.sort()
   SumLis = [0]*N
   for i,item in enumerate(lis):
      SumLis[i] += SumLis[i-1]+item
   for i,item in enumerate(lis):
      Output += lis[i] * (SumLis[-1]-SumLis[i])
      Output %= CONST
   print(Output)

      
def __starting_point():
    main()


__starting_point()
