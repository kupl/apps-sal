import sys
sys.setrecursionlimit(10**6)

def main(): 
   nbEntrees = int(input())
   nb = list(map(int, input().split()))
   maximum = max(nb)
   nb.remove(maximum)

   etendue = max(nb) - min(nb)
   nb.append(maximum)
   maximum = min(nb)
   nb.remove(maximum)
   
   etendue = min(etendue, max(nb) - min(nb))

   print(etendue)

main()
