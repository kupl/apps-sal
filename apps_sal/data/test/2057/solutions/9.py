import sys;

#sys.stdin = open("input.txt", "r");
#sys.stdout = open("output.txt", "w");

def ria():
    return [int(x) for x in input().split()];


n = int(input());
a = ria();
a = [0] + a;
time = [-1] * (n+1);
time[0] = 0;
tf = 0;


for i in range(1,n+1,1):
    if time[a[i]] != -1:
        time[i] = time[a[i]];
        time[a[i]] = -1;
    else:
        tf += 1;
        time[i] = tf;

tf += 1;

print(tf);
    
    


#sys.stdout.close();

