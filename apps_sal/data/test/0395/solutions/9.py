import sys;

#sys.stdin = open("input.txt", "r");
#sys.stdout = open("output.txt", "w");

def ria():
    return [int(x) for x in input().split()];

tf = 0;
a = ria();
n = len(a);
for i in range(n-2):
    for j in range(i+1, n-1, 1):
        for k in range(j+1, n, 1):
            if a[i] + a[j] + a[k] == (sum(a) / 2 ):
                tf = 1;
                break;
        if tf == 1:
            break;
    if tf == 1:
        break;

if ( tf == 1 ):
    print("YES");
else:
    print("NO");


#sys.stdout.close();

