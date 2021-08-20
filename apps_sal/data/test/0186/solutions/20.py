def __starting_point():
    (d, t) = list(map(int, input().split(' ')))
    result = 0
    i2 = d * 2
    i3 = t * 3
    cm = int(max(i2, i3) / 6)
    while cm > 0:
        if i2 + 2 < i3 + 3:
            i2 += 2
        elif i2 + 2 > i3 + 3:
            i3 += 3
        else:
            i2 += 2
            cm += 1
        cm -= 1
    print(max(i2, i3))
    '\n    if index2+common*2<=index3:\n        result = index3\n    else:\n        result = index2+common*2\n    if index2>=index3+common*3:\n        result = index2\n    '
    '\n    while common>0:\n        print (d,t,common,oldCommon)\n        if (d+1)*2<=(t+1)*3:\n            d+=1\n        else:\n            t+=1\n        index2 = d*2\n        index3 = t*3\n        print (index2,index3)\n        common = int(min(index2,index3)/6)\n\n        x = common \n        common-=oldCommon\n        oldCommon=x\n    print(max(index2,index3))\n    '


"\n\nC. Block Towers\ntime limit per test\n2 seconds\nmemory limit per test\n256 megabytes\ninput\nstandard input\noutput\nstandard output\n\nStudents in a class are making towers of blocks. Each student makes a (non-zero) tower by stacking pieces lengthwise on top of each other. n of the students use pieces made of two blocks and m of the students use pieces made of three blocks.\n\nThe students don’t want to use too many blocks, but they also want to be unique, so no two students’ towers may contain the same number of blocks. Find the minimum height necessary for the tallest of the students' towers.\nInput\n\nThe first line of the input contains two space-separated integers n and m (0\u2009≤\u2009n,\u2009m\u2009≤\u20091\u2009000\u2009000, n\u2009+\u2009m\u2009>\u20090) — the number of students using two-block pieces and the number of students using three-block pieces, respectively.\nOutput\n\nPrint a single integer, denoting the minimum possible height of the tallest tower.\nExamples\nInput\n\n1 3\n\nOutput\n\n9\n\nInput\n\n3 2\n\nOutput\n\n8\n\nInput\n\n5 0\n\nOutput\n\n10\n\nNote\n\nIn the first case, the student using two-block pieces can make a tower of height 4, and the students using three-block pieces can make towers of height 3, 6, and 9 blocks. The tallest tower has a height of 9 blocks.\n\nIn the second case, the students can make towers of heights 2, 4, and 8 with two-block pieces and towers of heights 3 and 6 with three-block pieces, for a maximum height of 8 blocks.\n\n"
__starting_point()
