import sys
n, m = [int(i) for i in input().split(' ')]


fconnection = [None] * n
bconnection = [None] * n

if m == 1:
    print(int((n + 1) * n / 2))
    return

svidetel = input().split(' ')
p = int(svidetel[0]) - 1
for current_pok in svidetel[1:]:
    q = int(current_pok) - 1
    fconnection[p] = q
    bconnection[q] = p
    p = q


for i in range(m - 1):
    svidetel = input().split(' ')
    p = int(svidetel[0]) - 1
#    try:
#        fconnection[fconnection.index(p)] = None
#    except ValueError:
#        pass
    bconnection[p] = None
    for current_pok in svidetel[1:]:
        q = int(current_pok) - 1
        if fconnection[p] != q:
            fconnection[p] = None
        if bconnection[q] != p:
            bconnection[q] = None
        p = q
    fconnection[p] = None
#    try:
#        bconnection[bconnection.index(p)] = None
#    except ValueError:
#        pass


is_bundled = [True] + [False] * (n - 1)
unbundled_count = n
current_bundle = []
number_of_variants = 0
research_deck = [0]

for i in range(n):
    if (fconnection[i] == None) and (bconnection[i] == None):
        number_of_variants += 1  # one distinct node
    elif bconnection[i] == None:
        # this is start of new run. check it.
        number_in_run = 1
        next_in_run = fconnection[i]
        while next_in_run is not None:
            number_in_run += 1
            next_in_run = fconnection[next_in_run]
        number_of_variants += int((1 + number_in_run) * number_in_run / 2)


# while unbundled_count >= 0:
#    #print(research_deck, current_bundle)
#    if research_deck:
#        c = research_deck.pop()
#        # check _to connection
#        if (connection[c] != None) and not is_bundled[connection[c]]:
#            research_deck.append(connection[c])
#        # check _from connection
#        try:
#            fr = connection.index(c)
#            if not is_bundled[fr]:
#                research_deck.append(fr)
#        except ValueError:
#            pass
#        current_bundle.append(c)
#        is_bundled[c] = True
#    else:
#        curlen = len(current_bundle)
#        number_of_variants += int((curlen + 1)*curlen/2)
#        unbundled_count -= curlen
#        current_bundle = []
#        if unbundled_count > 0:
#            research_deck = [is_bundled.index(False)]
#        else:
#            break
print(number_of_variants)
