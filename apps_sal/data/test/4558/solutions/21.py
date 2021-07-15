def main():
    X,t = list(map(int,input().split()))
    tmp = X-t
    if tmp<0:
        return 0
    else:
        return tmp

print((main()))

