n, m = map(int, input().split());
A = list(map(int, input().split()));
B = list(map(int, input().split()));
cnt = 0;
uka = 0;
ukb = 0;
suma = 0;
sumb = 0;
while 1:
    if uka >= n or ukb >= m:
        break;
    if suma <= sumb:
        suma = suma + A[uka];
        uka += 1;
    else:
        sumb = sumb + B[ukb];
        ukb += 1;
    if (suma == sumb):
        #print(suma, sumb);
        cnt = cnt + 1;
print(cnt + 1);
