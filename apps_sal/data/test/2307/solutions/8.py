n = eval(input())
arr = list(map(int, input().split()))
lucky = 0
for i in arr:
    if(i & 1):
        lucky -= 1
    else:
        lucky += 1
if(lucky > 0):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
