n, m, q = list(map(int, input().split()))
s = input()
t = input()
tt = [0] * 1111
for i in range(n - m + 1):
    j = 0
    while j < m and s[i + j] == t[j]: j += 1
    if j >= m: tt[i + 1] = 1
for i in range(1, n + 1): tt[i] += tt[i - 1]
for i in range(q):
    a, b = list(map(int, input().split()))
    if b - a + 1 < m:
        print(0)
        continue
    print(tt[b - m + 1] - tt[a - 1])


'''
////////////////      //////        ///////      //             ///////     //  //   //
////          //    ///   ///     ///    ///     //            ///  ///     ////     //
////    ////       ///     ///   ///      ///    //           /////////     ////     ///////
////     /////    ///       /// ///        ///   //          ///    ///     ////     //   //
//////////////     ///////////   ///////////     //////     ///     ///     //  //   //   //
'''
