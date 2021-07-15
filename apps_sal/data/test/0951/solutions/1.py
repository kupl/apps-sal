k = int(input());
n = int(input());
s = str(n);

arr = [int(x) for x in s];
arr.sort();
su = 0;
for i in range(len(arr)):
    su += arr[i];
tf = 0;
for i in range(len(arr)):
    if su >= k:
        break;
    else:
        su += 9-arr[i];
        tf += 1;

print(tf);

