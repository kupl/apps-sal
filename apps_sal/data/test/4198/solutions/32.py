a,b,x = map(int, input().split())

ok = 0 #買える
ng = pow(10,9)+1 #買えない

while abs(ng-ok)>1:
    mid = int((ok+ng)/2)
    c = a*mid+b*len(str(mid))
    if c <= x: #買える
        ok = mid
    else: #買えない
        ng = mid

print(ok)
