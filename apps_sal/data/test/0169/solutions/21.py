def __starting_point():
    r = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = 0
    if b - c >= a:
        d += r // a
        r = r % a
    else:
        if r >= b:
            t = (r - b + 1) // (b - c)
            d += t
            r -= t * (b - c)
            if r >= b:
                r -= b - c
                d += 1
        d += r // a
    '\n        while r>=b:\n            d+=r//b\n            r = r%b + c*(r//b)\n            print(d,r)\n        if r>=a:    d+=r//a\n    '
    print(d)


"\n\nA. Guest From the Past\ntime limit per test\n1 second\nmemory limit per test\n256 megabytes\ninput\nstandard input\noutput\nstandard output\n\nKolya Gerasimov loves kefir very much. He lives in year 1984 and knows all the details of buying this delicious drink. One day, as you probably know, he found himself in year 2084, and buying kefir there is much more complicated.\n\nKolya is hungry, so he went to the nearest milk shop. In 2084 you may buy kefir in a plastic liter bottle, that costs a rubles, or in glass liter bottle, that costs b rubles. Also, you may return empty glass bottle and get c (c\u2009<\u2009b) rubles back, but you cannot return plastic bottles.\n\nKolya has n rubles and he is really hungry, so he wants to drink as much kefir as possible. There were no plastic bottles in his 1984, so Kolya doesn't know how to act optimally and asks for your help.\nInput\n\nFirst line of the input contains a single integer n (1\u2009≤\u2009n\u2009≤\u20091018) — the number of rubles Kolya has at the beginning.\n\nThen follow three lines containing integers a, b and c (1\u2009≤\u2009a\u2009≤\u20091018, 1\u2009≤\u2009c\u2009<\u2009b\u2009≤\u20091018) — the cost of one plastic liter bottle, the cost of one glass liter bottle and the money one can get back by returning an empty glass bottle, respectively.\nOutput\n\nPrint the only integer — maximum number of liters of kefir, that Kolya can drink.\nSample test(s)\nInput\n\n10\n11\n9\n8\n\nOutput\n\n2\n\nInput\n\n10\n5\n6\n1\n\nOutput\n\n2\n\nNote\n\nIn the first sample, Kolya can buy one glass bottle, then return it and buy one more glass bottle. Thus he will drink 2 liters of kefir.\n\nIn the second sample, Kolya can buy two plastic bottle and get two liters of kefir, or he can buy one liter glass bottle, then return it and buy one plastic bottle. In both cases he will drink two liters of kefir.\n"
__starting_point()
