n = int(input())
a = [int(i) for i in input().split() if int(i)%2 == 0]
print("READY FOR BATTLE" if len(a) > n/2 else "NOT READY")
