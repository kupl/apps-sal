n = int(eval(input()))
arr = list(map(int, input().split()))
even = 0
for solder in arr:
    if solder % 2 == 0:
        even += 1

if even > n - even:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
