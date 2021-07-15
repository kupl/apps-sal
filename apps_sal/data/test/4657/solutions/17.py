n = int( input() )
result = []
for _ in range(n):
    (n,k) = list( map( int, input().split() ))
    a = list( map( int, input().split() ))
    nbOdds = 0
    for i in a:
        if i % 2 == 1:
            nbOdds += 1
    if nbOdds < k:
        result.append("NO")
    elif (nbOdds - k) % 2 == 0:
        result.append("YES")
        current = []
        for j in range(n):
            if a[j] % 2 == 1 and len(current) < k - 1:
                current.append(j+1)
        current.append(n)
        result.append( " ".join( list( map(str, current) ) ) )

    else:
        result.append("NO")
print( "\n".join(result) )



