#include "bits/stdc++.h"
using namespace std;
/*
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using ordered_set = tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>;
*/

#define all(x) begin(x), end(x)
#define sz(x) (int)x.size()

typedef long long ll;
const int mod = 1e9+7;
#define int ll

void solve(int tc) {
    int n, s;
    cin >> n >> s;
    vector<int> v(n);
    for (auto &x : v) cin >> x;
    vector<int> tr(1+n);
    tr[0] = s;
    for (int i = 1; i <= n; ++i) {
        int a = tr[i-1];
        int x = 0;
        while (a) {
            x += a%10;
            a /= 10;
        }
        tr[i] = tr[i-1] + x*x*x;
    }
    vector<vector<int>> dp(n+1, vector<int>(n+1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            dp[i][j] = dp[i-1][j] + v[i-1] * tr[j];
            if (j) dp[i][j] = max(dp[i][j], dp[i-1][j-1]);
        }
    }
    cout << *max_element(all(dp[n]));
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int tc = 1;
    //cin >> tc;
    for (int i = 1; i <= tc; ++i) solve(i);
    return 0;
}

