n = eval(input())
arr = list(map(int, input().split()))
ce = 0 
co = 0 
for i in arr:
    if i%2 == 0:
        ce += 1
    else:
        co+=1
if ce > co:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
