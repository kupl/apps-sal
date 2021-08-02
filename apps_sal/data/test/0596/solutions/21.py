def s():
    import datetime
    dt = datetime.datetime
    print(abs((dt(*list(map(int, input().split(':')))) - dt(*list(map(int, input().split(':'))))).days))


s()
