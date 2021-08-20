def __starting_point():
    n = int(input())
    lst = list(map(int, input().split(' ')))
    lst.sort()
    (h, i) = (0, 0)
    trav = []
    while i < n - 1:
        if i in trav:
            i += 1
            continue
        j = i + 1
        s = lst[i]
        while j < n:
            if lst[j] > s and j not in trav:
                h += 1
                s = lst[j]
                trav.append(j)
            j += 1
        trav.append(i)
        i += 1
    print(h)


'\nB. Beautiful Paintings\ntime limit per test\n1 second\nmemory limit per test\n256 megabytes\ninput\nstandard input\noutput\nstandard output\n\nThere are n pictures delivered for the new exhibition. The i-th painting has beauty ai. We know that a visitor becomes happy every time he passes from a painting to a more beautiful one.\n\nWe are allowed to arranged pictures in any order. What is the maximum possible number of times the visitor may become happy while passing all pictures from first to last? In other words, we are allowed to rearrange elements of a in any order. What is the maximum possible number of indices i (1\u2009≤\u2009i\u2009≤\u2009n\u2009-\u20091), such that ai\u2009+\u20091\u2009>\u2009ai.\nInput\n\nThe first line of the input contains integer n (1\u2009≤\u2009n\u2009≤\u20091000) — the number of painting.\n\nThe second line contains the sequence a1,\u2009a2,\u2009...,\u2009an (1\u2009≤\u2009ai\u2009≤\u20091000), where ai means the beauty of the i-th painting.\nOutput\n\nPrint one integer — the maximum possible number of neighbouring pairs, such that ai\u2009+\u20091\u2009>\u2009ai, after the optimal rearrangement.\nExamples\nInput\n\n5\n20 30 10 50 40\n\nOutput\n\n4\n\nInput\n\n4\n200 100 100 200\n\nOutput\n\n2\n\nNote\n\nIn the first sample, the optimal order is: 10,\u200920,\u200930,\u200940,\u200950.\n\nIn the second sample, the optimal order is: 100,\u2009200,\u2009100,\u2009200.\n'
__starting_point()
