def list2str(l):
    s = ""
    for d in l:
        s = s + str(d) + ' '
    s = s.strip()
    return s

def __starting_point():
    _input = input()
    data = list(map (int, _input.split() ) )
    n = data[0]
    m = data[1]

    avg = n // m
    plus = n - m * avg

    ans = list( [avg]*(m - plus) + [avg + 1]*plus )
    print( list2str(ans) )

__starting_point()
