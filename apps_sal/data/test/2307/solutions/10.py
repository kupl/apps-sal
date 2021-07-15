n = int(input().strip())
l = list(map(int, input().strip().split()))
unlucky = len([a for a in l if a%2])
print("READY FOR BATTLE" if n-unlucky > unlucky else "NOT READY")
