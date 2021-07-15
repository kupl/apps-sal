def main():
    h1,m1 = list(map(int,input().split(':')))
    h2,m2 = list(map(int,input().split(':')))
    min1 = h1*60+m1
    min2 = h2*60+m2

    diff = min2-min1
    mid = min1+(int(diff/2))
    hr = mid//60
    m = mid%60

    if hr < 10:
        hr = '0'+str(hr)

    if m < 10:
        m = '0'+str(m)

    print(str(hr)+':'+str(m))

main()

