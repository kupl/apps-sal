def generate_good_string(subs: list):
    (In, Out, S) = ({}, {}, set())
    for s in subs:
        if len(s) == 1:
            S.add(s)
        for (fr, to) in zip(s, s[1:]):
            if fr != In.get(to, fr) or to != Out.get(fr, to):
                return print('NO')
            (Out[fr], In[to]) = (to, fr)
    (Outset, Inset) = (set(Out), set(In))
    S -= set.union(Outset, Inset)
    for s in Outset - Inset:
        while Out.get(s[-1]):
            s += Out.pop(s[-1])
        S.add(s)
    print('NO' if Out else ''.join(sorted(S)))


substrings = [input() for _ in range(int(input()))]
generate_good_string(substrings)
