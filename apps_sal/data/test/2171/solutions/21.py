# cook your dish here
try:
    n = int(input())
    g = n % 6
    if(g == 0 or g == 1 or g == 3 or g == 6):
        print('yes')
    else:
        print('no')
except:
    pass
