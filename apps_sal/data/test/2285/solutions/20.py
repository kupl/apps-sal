for _ in range(int(input())):
    D = input()
    print(':'.join(d.zfill(4) for d in D.replace('::', ':' * (9 - D.count(':')))
                                        .split(':')))
