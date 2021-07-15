def main():
   N = int(input())
   S = input()
   S = list(S)
   size = len(S)
   for i in range(size):
      num = ord(S[i]) + N
      if(num > 90):
         num -= 26
      S[i] = chr(num)
   for i,item in enumerate(S):
      print(item,end="")
   print("")
def __starting_point():
    main()


__starting_point()
